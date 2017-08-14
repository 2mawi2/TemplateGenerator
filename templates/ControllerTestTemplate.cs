using System;
using <#package#>;
using <#package#>.Controllers;
using Moq;
using Persistence<#package#>;
using Xunit;

namespace UnitTests.<#package#>.<#package#>.Controllers
{
    public class <#name#>ControllerTests : IDisposable
    {
        private readonly MockRepository _mockRepository;

        private readonly Mock<I<#name#>Repository> _mock<#name#>Repository;
        
        public <#name#>ControllerTests()
        {
            _mockRepository = new MockRepository(MockBehavior.Strict);
            _mock<#name#>Repository = _mockRepository.Create<I<#name#>Repository>();
        }

        public void Dispose()
        {
            _mockRepository.VerifyAll();
        }

        private I<#name#>Controller Create<#name#>Controller()
        {
            return new <#name#>Controller(_mock<#name#>Repository.Object);
        }
    }
}